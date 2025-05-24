from name_function import get_formatted_name

def test_first_last_name():
    #测试没有中间值时输出
    formatted_name = get_formatted_name('zheng', 'chen')
    assert formatted_name == 'Zheng Chen'

def test_first_middle_name():
    #测试有中间值时输出
    formatted_name = get_formatted_name('zheng', 'wang', 'lin')
    assert formatted_name =='Zheng Lin Wang'