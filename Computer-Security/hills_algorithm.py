from numpy import matrix
from numpy import array
#================Hill's algorithm for encryption=================
def inverse_alphabet_values(value):
    x=0
    if(value[x]==0):
        value='a'
    elif(value[x]==1):
        value='b'
    elif(value[x]==2):
        value='c'
    elif(value[x]==3):
        value='d'
    elif(value[x]==4):
        value='e'
    elif(value[x]==5):
        value='f'
    elif(value[x]==6):
        value='g'
    elif(value[x]==7):
        value='h'
    elif(value[x]==8):
        value='i'
    elif(value[x]==9):
        value='j'
    elif(value[x]==10):
        value='k'
    elif(value[x]==11):
        value='l'
    elif(value[x]==12):
        value='m'
    elif(value[x]==13):
        value='n'
    elif(value[x]==14):
        value='o'
    elif(value[x]==15):
        value='p'
    elif(value[x]==16):               
        value='q'
    elif(value[x]==17):    
        value='r'
    elif(value[x]==18):
        value='s'
    elif(value[x]==19):
        value='t'
    elif(value[x]==20):
        value='u'
    elif(value[x]==21):
        value='v'
    elif(value[x]==22):
        value='w'
    elif(value[x]==23):
        value='x'
    elif(value[x]==24):
        value='y'
    elif(value[x]==25):
        value='z'
    elif(value[x]==26):
        value=' '
    else:
        value="Hay un error en esta funcion"
    return value

def alphabet_values(value):
    """El problema con los diccionarios es que una vez que se recorren por
        completo no hay manera de volver a iniciarlo en cero a menos que 
        se vuelva a entrar a la funcion"""
    x=0
    alphabet={"a":'0',
              "b":'1',
              "c":'2',
              "d":'3',
              "e":'4',
              "f":'5',
              "g":'6',
              "h":'7',
              "i":'8',
              "j":'9',
              "k":'10',
              "l":'11',
              "m":'12',
              "n":'13',
              "o":'14',
              "p":'15',
              "q":'16',
              "r":'17',
              "s":'18',
              "t":'19',
              "u":'20',
              "v":'21',
              "w":'22',
              "x":'23',
              "y":'24',
              "z":'25',
              " ":'26'}
	                         
    for letter, number in alphabet.iteritems():        
        if(x<len(value)):
            if (value[x]==letter):
                value[x]=int (number)                
                x=x+1                   
    return value

def matrix_operation(column_vector):
    A     =   matrix (column_vector)
    result=   (Key*A)%27
    return result

def inverse_matrix_operation(column_vector2):   
    determinant=det(Key)
    important_number=inverse_modulo(determinant)
    Transpose=Key.T
    #print Transpose
    """c00,c10,c01,c11 are the cofactors of the matrix. Python
    uses the notation of rows-columns."""
    c00=Transpose[1,1] #*important_number %27
    c10=Transpose[0,1] #*important_number %27
    c01=Transpose[1,0] #*important_number %27
    c11=Transpose[0,0] #*important_number %27
    inverse_matrix=(((matrix([[c00,-c01],[-c10,c11]])*important_number)%27)*column_vector2)%27
    return inverse_matrix
    
def inverse_modulo(determinant):
    flag=False
    magic_number=0
    while(flag==False):
        result=magic_number*determinant
        result=result%27
        if(result==1): #Si se cumple entonces cumpliste con el modulo inverso
            flag=True
            return magic_number
        #else:
        #    return "I am still looking for the inverse modulo" #Aqui esta el error
        magic_number=magic_number+1
    
def matrix_to_list(values):
    lista=list()
    for x in array(values).flat:
        lista.append(x)
    return lista

def det(l):
    c00=Key[0,0]
    c10=Key[1,0]
    c01=Key[0,1]
    c11=Key[1,1]
    return (c00*c11-c01*c10)

        
#========================Initiate program==============================
given_text=raw_input("Please, give me your text (more than three words):") 
Key=matrix([[3,2],[5,7]])
i=0
j=1
new_value=list()
#=============Substitute each letter with its given number==================
while(i<len(given_text)):
    message_conversion = list ((given_text[i:j]).lower()) #Lo pongo en lista para que pueda hacer el i:j.
    conversion	   = alphabet_values(message_conversion)
    i=i+1
    j=j+1
    new_value.append(conversion) #Los valores previos de la lista deben anexarse a la previa.
#print new_value
#===============================Matrix operation========================
y=0
z=2
matrix_result=list()
while(y<len(given_text)):
    selected_matrix  =  new_value[y:z]
    matrix_result.append(matrix_operation(selected_matrix))
    y=y+2
    z=z+2
#print "numbers of the matrix==>"+str(matrix_result)
matrix_to_list_numbers=matrix_to_list(matrix_result)
#print "lista de numeros==>"+str(matrix_to_list_numbers)
#==================Conversion from number to letter========================
count=0
start=0
end=1
list_with_new_values=list()
while(count<len(matrix_to_list_numbers)):
    numbers_to_letters=inverse_alphabet_values(matrix_to_list_numbers[start:end])
    #lo de arriba ya esta en lista, por tanto, no necesito realizar un cast
    list_with_new_values.append(numbers_to_letters)
    count=count+1
    start=start+1
    end=end+1
print "Encrption complete:"
print list_with_new_values
#========================Decryption process========================
inicias=0
final=1
new_value2=list()
#=============Substitute each letter with its given number==================
while(inicias<len(list_with_new_values)):
    decrypt1 	   = alphabet_values(list_with_new_values[inicias:final]) 
    inicias            = inicias+1
    final              = final+1
    new_value2.append(decrypt1) #Los valores previos de la lista deben anexarse a la previa.
#print new_value2
#===================Inverse Matrix Operation========================
commence=0
alafin=2
matrix_result_inverso=list()
while(commence<len(new_value2)):
    matrix_inverse_operation_value  =  new_value2[commence:alafin]
    matrix_result_inverso.append(inverse_matrix_operation(matrix_inverse_operation_value))
    commence=commence+2
    alafin=alafin+2
print "numbers of the inverse matrix==>"+str(matrix_result_inverso)
#====================Conversion from numbers to letters==================
matrix_to_list_numbers2=matrix_to_list(matrix_result_inverso)
counter=0
almostdone=0
almostdone2=1
list_with_new_values2=list()
while(counter<len(matrix_to_list_numbers2)):
    numbers_to_letters2=inverse_alphabet_values(matrix_to_list_numbers2[almostdone:almostdone2])
    #lo de arriba ya esta en lista, por tanto, no necesito realizar un cast
    list_with_new_values2.append(numbers_to_letters2)
    counter      = counter+1
    almostdone   = almostdone+1
    almostdone2  = almostdone2+1
print "Decryption complete:"
print list_with_new_values2


