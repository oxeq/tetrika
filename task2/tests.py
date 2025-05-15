from unittest.mock import Mock, mock_open
import solution

def test_get_animals_count_single_page(mocker):
    """Тест для одной страницы без перехода на следующую"""
    html = '''
    <div id="mw-pages">
        <div class="mw-category-group">
            <a href="/wiki/Акула">Акула</a>
            <a href="/wiki/Аист">Аист</a>
            <a href="/wiki/Барсук">Барсук</a>
        </div>
    </div>
    '''
    mock_response = Mock()
    mock_response.text = html
    mocker.patch('solution.requests.get', return_value=mock_response)

    counts = solution.get_animals_count()
    assert counts.get('А') == 2
    assert counts.get('Б') == 1

def test_get_animals_count_pagination(mocker):
    """Тест с переходом на следующую страницу"""
    html_page1 = '''
    <div id="mw-pages">
        <div class="mw-category-group">
            <a href="/wiki/Акула">Акула</a>
            <a href="/wiki/Аист">Аист</a>
        </div>
        <a href="/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Б">Следующая страница</a>
    </div>
    '''
    html_page2 = '''
    <div id="mw-pages">
        <div class="mw-category-group">
            <a href="/wiki/Барсук">Барсук</a>
        </div>
    </div>
    '''
    mock_response1 = Mock()
    mock_response1.text = html_page1
    mock_response2 = Mock()
    mock_response2.text = html_page2

    mocker.patch('solution.requests.get', side_effect=[mock_response1, mock_response2])

    counts = solution.get_animals_count()
    assert counts.get('А') == 2
    assert counts.get('Б') == 1

def test_save_to_csv(mocker):
    """Тест сохранения в CSV-файл"""
    counts = {'А': 3, 'Б': 1}
    m = mock_open()
    mocker.patch('builtins.open', m)
    solution.save_to_csv(counts, filename='test.csv')
    m.assert_called_once_with('test.csv', 'w', newline='', encoding='utf-8')
    handle = m()
    written = ''.join(call.args[0] for call in handle.write.call_args_list)
    assert 'А,3' in written
    assert 'Б,1' in written
