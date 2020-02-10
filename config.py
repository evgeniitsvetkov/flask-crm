class Config:
    SECRET_KEY= "secret_key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    # postgres://xyybtbtfxjfvpw:942e4e024fdf4933ebc807ab5fa5f8889c05eddd02a128a2bbf488dcdc47a838@ec2-54-195-252-243.eu-west-1.compute.amazonaws.com:5432/d8cgf8nqkqm44l
    SQLALCHEMY_TRACK_MODIFICATIONS = False
