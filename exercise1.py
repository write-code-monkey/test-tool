shuju = [{'title': '一级标题', 'topics': [{'title': '二级标题', 'topics': [{'title': '三级标题', 'topics': [{'title': '四级标题', 'makers': ['priority-1'], 'topics': [{'title': '五级标题', 'topics': [{'title': '六级标题'}]}]}]}, {'title': '测试点2', 'topics': [{'title': '用例名称', 'makers': ['priority-2'], 'topics': [{'title': '操作步骤', 'topics': [{'title': '预期结果'}]}]}]}, {'title': '测试点2', 'topics': [{'title': '用例名称', 'makers': ['priority-3'], 'topics': [{'title': '操作步骤', 'topics': [{'title': '预期结果'}]}]}]}]}]}, {'title': '业务大类2', 'topics': [{'title': '业务小类2-1', 'topics': [{'title': '测试点2-1-1', 'topics': [{'title': '用例名称', 'makers': ['priority-3'], 'topics': [{'title': '操作步骤', 'topics': [{'title': '预期结果'}]}]}]}]}]}, {'title': '后台', 'topics': [{'title': '运营内容管理', 'topics': [{'title': '测试点1', 'topics': [{'title': '页面展示', 'makers': ['priority-2'], 'topics': [{'title': '1.查看页面', 'topics': [{'title': '1.展示页面'}]}, {'title': '2.点击【确认】', 'topics': [{'title': '2.提示请输入信息'}]}, {'title': '3.点击【取消】', 'topics': [{'title': '3.返回到上一级页面'}]}]}]}, {'title': '测试点2', 'topics': [{'title': '新增运营内容展示及逻辑校验', 'makers': ['priority-1'], 'topics': [{'title': '1.新增运营内容', 'topics': [{'title': '1.正常'}]}]}]}]}]}]


for first_title in shuju:
    print(first_title)
    for secound_title in first_title['topics']:
        print(secound_title)
        for third_title in secound_title['topics']:
            print(third_title)

