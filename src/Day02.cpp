#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <regex>

using namespace std;

int main (int argc, char* argv[])
{
  ifstream input_file(argv[1]);
  if (input_file.is_open()){
    string line;
    int part1 = 0;
    int part2 = 0;
    regex regexp ("(\\d+)-(\\d+) (\\w): (\\w+)");
    smatch matches;
    while ( getline (input_file,line) ) {
      if (regex_match(line,matches,regexp)){
        int val_1 = std::stoi(matches[1]);
        int val_2 = std::stoi(matches[2]);
        char rule = std::string(matches[3]).at(0);
        string pass = std::string(matches[4]);
        int rule_count = std::count(pass.begin(),pass.end(),rule);
        part1+=rule_count>=val_1&&rule_count<=val_2;
        part2+=(pass.at(val_1-1)==rule) != (pass.at(val_2-1)==rule);
      }
    }
    input_file.close();
    cout<<to_string(part1)<<endl;
    cout<<to_string(part2)<<endl;
    return 0;
  }
  else{
    return 1;
  }
}
