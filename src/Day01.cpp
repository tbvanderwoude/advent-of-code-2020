#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

vector<int> get_input()
{
  vector<int> numbers;
  string line;
  ifstream myfile ("inputs/input01.txt");
  if (myfile.is_open()){
    while ( getline (myfile,line) ) {
      numbers.push_back(std::stoi(line));
    }
    myfile.close();
  }
  return numbers;
}

int main ()
{
  vector<int> lines = get_input();
  int part1 = -1;
  int part2 = -1;
  for (auto x : lines){
    for (auto y : lines){
      if (x+y==2020)
      {
        part1 = x*y;
      }
      for (auto z : lines){
        if (x+y+z==2020)
        {
          part2 = x*y*z;
        }
      }
    }
  }
  cout<<to_string(part1)<<endl;
  cout<<to_string(part2)<<endl;
  return 0;
}
