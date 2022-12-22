class Config:
    SECRET_KEY = 'Sup3r_s3cr3t'
    WTF_CSRF_SECRET_KEY = 'Sup3r_s3cr3t0'
    MYSQL_HOST = '/cloudsql/wgweb-production:southamerica-east1:wg-mysql1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Kima.2020'
    MYSQL_DB = 'WG'

class DevelopmentConfig(Config):
    DEBUG = True
    

config = {
    'development' : DevelopmentConfig
}