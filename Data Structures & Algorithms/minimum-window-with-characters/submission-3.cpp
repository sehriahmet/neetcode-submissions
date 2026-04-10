class Solution {
public:
    string minWindow(string s, string t) {
        if (s.size() < t.size()) return "";

        int start = 0;
        int min_start = 0;
        int have_count = 0;
        int need_count;
        int length = s.size() + 1;

        std::unordered_map<char, int> have;
        std::unordered_map<char, int> need; 

        for (int i = 0; i < t.size(); i++) {
            if (need.count(t.at(i))) 
            need[t.at(i)] += 1;
            else
            need[t.at(i)] = 1;
            have[t.at(i)] = 0;
        }

        need_count = need.size();

        for (int i = 0; i < s.size(); i++) {
            if (have.count(s.at(i))) {
                have[s.at(i)]++;
                cout<<s.at(i)<<" "<<have[s.at(i)]<<" "<< need[s.at(i)]<<" "<<have_count<<" "<<need_count<<endl;
                if (have[s.at(i)] == need[s.at(i)]) {
                    have_count++;
                    while (have_count == need_count) {
                        cout<<"start: "<<start<<" "<<i<<endl;
                        if (length > i-start+1) {
                            length = i-start+1;
                            min_start = start;
                        }
                        if (have.count(s.at(start))) {
                            have[s.at(start)]--;
                            if (have[s.at(start)] < need[s.at(start)]) have_count--;
                        }
                        start++;
                    }
                }
            }

        }

        if (length == s.size() + 1) return "";
        
        return s.substr(min_start, length);
    }
};
