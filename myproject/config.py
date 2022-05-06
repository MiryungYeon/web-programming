import os # 디렉터리를 알기 위함

BASE_DIR = os.path.dirname(__file__) # 대문자 변수는 환경변수 값이라고 생각, 잘 변하지 않는 초기 값

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False # 이벤트 처리하는 옵션