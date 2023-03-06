import uuid # генерирует случайные объекты из 128 бит в качестве идентификаторов
from datetime import datetime

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status # Starlette - это легкий фреймворк / инструментарий OSGI 

from app.forms import UserLoginForm, UserCreateForm
from app.models import connect_db, User, AuthToken
from app.authentication import check_auth_token
from app.utils import get_password_hash


router = APIRouter()


@router.get('/')
def index():
  return {'status': 'Ok'}


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=Depends(connect_db)):
  user = database.query(User).filter(User.email == user_form.email).one_or_none()
  if not user or get_password_hash(user_form.password) != user.password:
    return {'error': 'Email/password doesnt match'}

  auth_model = AuthToken(token=str(uuid.uuid4()), user_id=user.id, created_at=datetime.now())
  database.add(auth_model)
  database.commit()
  return {'auth_token': auth_model.token}


@router.get('/user', name='user:get')
def get_user(token: AuthToken = Depends(check_auth_token), database=Depends(connect_db)):
  user = database.query(User).filter(User.id == token.user_id).one_or_none()
  return {'user': user.get_filtered_data()}


@router.post('/user', name='user:create')
def create_user(user_form: UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
  exists_user = database.query(User.id).filter(User.email == user_form.email).one_or_none()
  if exists_user:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='Email already exists',
    )

  new_user = User(
    email=user_form.email,
    password=get_password_hash(user_form.password),
    first_name=user_form.first_name,
    last_name=user_form.last_name,
    nickname=user_form.nickname
  )
  database.add(new_user)
  database.commit()
  return {'user_id': new_user.id}




