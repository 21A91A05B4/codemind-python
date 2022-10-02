t=int(input())
while(t):
    s=input()
    
    st=[]
    st2=[]
    k=0
    for i in s:
        if i in '({[':
            st.append(i)
        
        else:
            if len(st)==0:
                k=1
                break
            else:
                if i==')' and st[-1]=='(':
                    st.pop()
                elif i==']' and st[-1]=='[':
                    st.pop()
                elif i=='}' and st[-1]=='{':
                    st.pop()
            
    #print(st)
    #print(st2)
    if len(st)==0 and k==0:
        print('True')
    else:
        print('False')
    t-=1