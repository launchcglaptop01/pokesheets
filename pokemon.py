import requests
import sys

def lookupInput(input):
    # If input is not empty then lookup pokemon
    if (input):
        response = requests.get('https://pokeapi.co/api/v2/pokemon/' + input + '/')
        if (response): 
            # If response does contains return information
            # Then turn response to json
            rjson = response.json()
            # Print out id, name, weight
            print (rjson['id'],end="")
            print (',',end="")
            print (rjson['name'],end="")
            print (',',end="")
            print (rjson['weight'],end="")
            if (rjson['types']):
                # If lookup item contains types then print them out with
                # | as separator 
                print (',',end="")
                first=1
                for type in rjson['types'] :
                    if (first==1):
                        first=0
                    else:
                        print ('|',end="")
                    print (type['type']['name'], end="")
            # Do this print for linefeed before next row
            print("")
        else:
            # Print [input name] Not Found. In stderr
            print("Warning: Pokemon=" + input + " Not Found.", file=sys.stderr)

def main():

    #Removing the first argument which contains this program name but it is not an input parameter
    arguments=sys.argv[1::]
    print("ID,NAME,WEIGHT,TYPES")
    for input in sys.argv[1::]:
         # For each valid parameter
        try:
            lookupInput(input)
        except:
            # Exception. Print error and Stack trace
            print("")
            print("Error:",sys.exc_info()[0],"occured.", file=sys.stderr) 
            print ('-'*60)
            traceback.print_exc(file=sys.stderr)
            print ('-'*60)

if __name__ == '__main__':
    # Run the main function
    main()
   
   


