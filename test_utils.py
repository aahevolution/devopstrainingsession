from utils import greet

def test_greet(capsys):
    greet("ChatGPT")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, ChatGPT!"
