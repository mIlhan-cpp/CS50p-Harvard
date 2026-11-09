from um import count

def main():
    test_case()
    test_word_um()
    test_white_space()

def test_case():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_word_um():
    assert count('yummy') == 0
    assert count('Mumbai') == 0

def test_white_space():
    assert count('Hello, um world') == 1
    assert count('Um?') == 1

if __name__ == "__main__":
    main()