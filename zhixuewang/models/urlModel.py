BASE_URL = "https://www.zhixue.com"

# Login
SERVICE_URL = f"{BASE_URL}:443/ssoservice.jsp"
SSO_URL = f"https://open.changyan.com/sso/login?sso_from=zhixuesso&service={SERVICE_URL}"
INFO_URL = f"{BASE_URL}/container/container/student/account/"
CHANGE_PASSWORD_URL = f"{BASE_URL}/portalcenter/home/updatePassword/"
TEST_PASSWORD_URL = f"{BASE_URL}/weakPwdLogin/?from=web_login"
XTOKEN_URL = f"{BASE_URL}/addon/error/book/index"

# Exam
GET_EXAM_URL = f"{BASE_URL}/zhixuebao/zhixuebao/main/getUserExamList/"
GET_MARK_URL = f"{BASE_URL}/zhixuebao/zhixuebao/feesReport/getStuSingleReportDataForPK/"
GET_PAPERID_URL = f"{BASE_URL}/zhixuebao/report/exam/getReportMain"
GET_ORIGINAL_URL = f"{BASE_URL}/zhixuebao/report/checksheet/"

# Person
GET_FRIEND_URL = f"{BASE_URL}/zhixuebao/zhixuebao/friendmanage/"
INVITE_FRIEND_URL = f"{BASE_URL}/zhixuebao/zhixuebao/addFriend/"
DELETE_FRIEND_URL = f"{BASE_URL}/zhixuebao/zhixuebao/delFriend/"
GET_CLAZZS_URL = GET_FRIEND_URL
GET_CLASSMATES_URL = f"{BASE_URL}/zhixuebao/zhixuebao/getClassStudent/"