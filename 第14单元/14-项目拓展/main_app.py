import pymongo


# 建立连接
client = pymongo.MongoClient()
# 创建年级数据库
db = client['gread']
# 创建班级集合
clasdds = db['clsd']

# 一条学生数据
student = {'name': '壮猿',
           'gender': '男',
           'age':'11'}

# 向班级集合中插入一条学生数据
clasdds.insert_one(student)
