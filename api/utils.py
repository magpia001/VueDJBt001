def obj_to_post(obj, flag=True):
    """
    obj의 각 속성을 serialize 해서, dict로 변환함
    serialize: python object ->> (기본 타입) int, float, str 으로 형변환 하는 과정
    :param obj:
    :param flag: True(모두 보냄, /api/post/99/ 용), False(일부 보냄, /api/post/list/ 용)
    :return:

    vars() : 데이터를 dict type으로 변형하는 python 내장 함수
    """
    post = dict(vars(obj))

    if obj.category:
        post['category'] = obj.category.name
    else:
        post['category'] = 'NoCategory'
    
    if obj.tags:
        post['tags'] = [t.name for t in obj.tags.all()]
    else:
        post['tags'] = []
    
    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = f'https://picsum.photos/id/{obj.id}/900/400'

    if obj.update_dt:
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_dt'] = '9999-12-31 00:00:00'
    
    # django manage.py shell에서 값 vars(Post.objects.all()[0]) 결과 확인하기
    # vars() 함수 결과에는 manytomay 필드 결과는 없음
    del post['_state'], post['category_id'], post['create_dt']

    # /api/post/list/ 일경우, 삭제
    if not flag:   
            del post['tags'], post['update_dt'], post['description'], post['content']

    return post