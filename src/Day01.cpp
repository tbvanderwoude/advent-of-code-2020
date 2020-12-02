#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main (int argc, char* argv[])
{
  ifstream input_file(argv[1]);
  string line;
  vector<int> lines;
  while ( getline (input_file,line) ) {
    lines.push_back(std::stoi(line));
  }
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
