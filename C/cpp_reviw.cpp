#include <stdio.h>
#include <iostream>
#include <unistd.h>
#include <vector>
#include <map>
#include <set>
using namespace std;

class Base {
    public:
    virtual ~Base(){};
};
class Derived: public Base {};


void hello()
{
    const char *s="hello,world!";
    cout<<s<<endl;
}

void type_cast()
{
    cout<<"static cast:"<<endl;
    int i = 10;
    float j = static_cast<float>(i);
    cout<<j<<endl;

    cout<<"dynamic cast:"<<endl;
    Base* ptr_base = new Derived();
    Derived* ptr_derived = dynamic_cast<Derived*>(ptr_base);

    cout<<"const cast"<<endl;
    const int x = 10;
    int &r = const_cast<int&>(x);

}

void memory_new_delete()
{
    int *array = new int[20];
    for (int i=0;i<20;i++)
    {
        array[i] = i;
    }
    for (int i=0;i<20;i++)
    {
        printf("array[%d]=[%d]\n", i, array[i]);
    }    
    delete [] array;
}

int vector_practise()
{
    vector<int> my_vector;
    for(int i = 0; i<100; i++)
    {
        my_vector.push_back(i);
    }
    cout<<"vector size is:["<<my_vector.size()<<"]"<<endl;
    auto delete_it = my_vector.begin()+3;
    my_vector.erase(delete_it);
    for(auto it=my_vector.begin(); it!=my_vector.end(); it++)
    {
        cout<<"vector item are:["<<*it<<"]"<<endl;
    }    
    my_vector.pop_back();
    my_vector.pop_back();

    for(auto it=my_vector.begin(); it!=my_vector.end(); it++)
    {
        cout<<"vector item are:["<<*it<<"]"<<endl;
    } 

    my_vector.clear();
    cout<<"vector size is:["<<my_vector.size()<<"]"<<endl;
    return 0;
}

void map_practise()
{
    map<string, int> s_i_map;
    string key="1";
    s_i_map[key] = 3;
    cout<<s_i_map[key]<<endl;
    for(auto iter=s_i_map.begin();iter!=s_i_map.end();iter++)
    {
        cout<<iter->first<<"->"<<iter->second<<endl;
    }
    if(s_i_map.find(key) != s_i_map.end())
    {
        cout<<"key "<<key<<" exist!"<<endl;
        s_i_map.erase(key);
        s_i_map.clear();

    }
}

void set_practise()
{
    set<int> mySet;
    for(auto i=0;i<10;i++)
    {
        mySet.insert(i);
        mySet.insert(i);
    }
    cout<<"size of mySet is :["<<mySet.size()<<"]"<<endl;
    int x = 8;
    if(mySet.find(x)!=mySet.end())
    {
        cout<<"x in my Set!"<<endl;
    }
    else
    {
        cout<<"no, in my my Set!"<<endl;
    }
    mySet.erase(8);
    if(mySet.find(x)!=mySet.end())
    {
        cout<<"x in my Set!"<<endl;
    }
    else
    {
        cout<<"no, in my my Set!"<<endl;
    }

}

int main()
{

    //vector<int> my_vector;
    
    //vector_practise();

    //map_practise();
    set_practise();

    return 0;
}