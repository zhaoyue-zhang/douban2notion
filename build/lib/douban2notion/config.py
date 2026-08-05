
RICH_TEXT = "rich_text"
URL = "url"
RELATION = "relation"
NUMBER = "number"
DATE = "date"
FILES = "files"
STATUS = "status"
TITLE = "title"
SELECT = "select"
MULTI_SELECT = "multi_select"

book_properties_type_dict = {
    "书名":TITLE,
    "短评":RICH_TEXT,
    "ISBN":RICH_TEXT,
    "豆瓣链接":URL,
    "作者":RELATION,
    "评分":SELECT,
    "封面":FILES,
    "分类":RELATION,
    "状态":STATUS,
    "日期":DATE,
    "简介":RICH_TEXT,
    "豆瓣链接":URL,
    "出版社":MULTI_SELECT,
    # 用户在 Notion 书架库加的 number 属性，用于 github_heatmap 累加
    "Count": NUMBER,
}

TAG_ICON_URL = "https://www.notion.so/icons/tag_gray.svg"
USER_ICON_URL = "https://www.notion.so/icons/user-circle-filled_gray.svg"
BOOK_ICON_URL = "https://www.notion.so/icons/book_gray.svg"


movie_properties_type_dict = {
    "电影名":TITLE,
    "短评":RICH_TEXT,
    # "ISBN":RICH_TEXT,
    # "链接":URL,
    # "导演":RELATION,  # 暂不写：fork 0.0.7 没 actor_database_id，调 get_relation_id 会 fail
    # "演员":MULTI_SELECT,  # 暂不写：Notion 端 schema 是 relation，类型不匹配
    # "Sort":NUMBER,
    "封面":FILES,
    "分类":RELATION,
    "状态":STATUS,
    "类型":SELECT,
    "评分":SELECT,
    # "阅读时长":NUMBER,
    # "阅读进度":NUMBER,
    # "阅读天数":NUMBER,
    "日期":DATE,
    "简介":RICH_TEXT,
    # "开始阅读时间":DATE,
    # "最后阅读时间":DATE,
    # "简介":RICH_TEXT,
    # "书架分类":SELECT,
    # "我的评分":SELECT,
    "豆瓣链接":URL,
    # 跟 BOOK 一样，用户在 Notion 电影库加的 number 属性，用于 github_heatmap 累加
    "Count": NUMBER,
}
