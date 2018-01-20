import sys

def init():
    name = sys.argv[1]
    adj = raw_input("Please input an adjective: ")
    biz = raw_input("Please input an business: ")
    aml = raw_input("Please input an animal: ")
    noz = raw_input("Please input an noise: ")
    return(name, adj, biz, aml, noz)

def madlib(name, adj, biz, aml, noz):
    print("\n" + name)
    print(adj + " McDonald had a " + biz + ", E-I-E-I-O")
    print("and on that " + biz + " he had a " + aml + ", E-I-E-I-O")
    print("with a " + noz + " " + noz + " here")
    print("and a " + noz + " " + noz + " there,")
    print("here a " + noz + " there a " + noz + ",")
    print("every where a " + noz + " " + noz + ",")
    print(adj + " McDonald had a " + biz + ", E-I-E-I-O")

def main():
    name, adj, biz, aml, noz = init()
    madlib(name, adj, biz, aml, noz)

main()
