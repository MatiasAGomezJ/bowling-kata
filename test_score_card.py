from ScoreCard import ScoreCard    
import pytest

@pytest.mark.ScoreCard
def test_funciona1():
    # Hitting pins total = 60
    pins = "12345123451234512345"
    total = 60
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona2():
    # test symbol -
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona3():
    pins = "9-3561368153258-7181"
    total = 82
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona4():
    # test spare not extra
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona5():
    # test strike
    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona6():
    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona7():
    # two strikes in a row is a double
    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona8():
    # three strikes in a row is a triple
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona9():
    # one pin extra roll
    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona10():
    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona11():
    # two strikes in extra rolls
    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    scoreCard = ScoreCard(pins)

@pytest.mark.ScoreCard
def test_funciona12():
    # one strike in extra roll
    pins = "8/549-XX5/53639/9/X"
    total = 149
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona13():
    # spare in extra roll
    pins = "X5/X5/XX5/--5/X5/"
    total = 175
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total

@pytest.mark.ScoreCard
def test_funciona14():
    # 12 strikes is a “Thanksgiving Turkey”
    # 2 strikes in extra rolls
    pins = "XXXXXXXXXXXX"
    total = 300
    scoreCard = ScoreCard(pins)
    assert scoreCard.getTotal() == total