"""currency.py: Calculating the currency amount according to the exchange rate.

__author__ = "Bai Yuchen"
__pkuid__  = "1800011798"
__email__  = "1800011798@pku.edu.cn"
"""

from urllib.request import urlopen

def exchange(currency_from,currency_to,amount_from):
    """exchange function exchanges amount_from currency of currency_from kind of currency to currency_to kind of currency
    and returns the amount of currency of  currency_to kind of currency.
    """
    c_f=currency_from
    c_t=currency_to
    a_f=amount_from
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+c_f+'&to='+c_t+'&amt='+a_f)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    list_total=list(jstr)
    list_number=[]
    begin_character=len(list(a_f))
    for item in list_total:
        if item.isdigit()==True or item=='.':
            list_number=list_number+[item]
    answerlist=list_number[begin_character:]
    answer=''
    for item in answerlist:
        answer=answer+item
    amount_to=float(answer)
    return amount_to

def test_exchange():
    """exchange_test tests whether the function exchange works well.
    """
    assert(exchange('CNY','JPY','100')==1625.7643642095)

def testAll():
    """test all cases"""
    test_exchange()
    print("All tests passed")

def main():
    """main module
    """
    currency_from=input()
    currency_to=input()
    amount_from=input()
    testAll()
    print(exchange(currency_from,currency_to,amount_from))   

if __name__ == '__main__':
    main()