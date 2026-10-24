import java.util.*;

class Solution {
    public int solution(String[][] relation) {
        int row = relation.length;
        int column = relation[0].length;
        
        Set<Integer> candidateKeys = new HashSet<>();
        
        for (int mask=1; mask<(1<<column); mask++) {
                    
            // 최소성 검사 -> 이미 후보키에 있음
            boolean minimal = true;
            for (int candidate : candidateKeys) {
                if ((mask & candidate) == candidate) {
                    minimal = false;
                    break;
                }
            }
            if (!minimal) continue;
            
            // 유일성 검사
            Set<String> set = new HashSet<>();
            
            for (int i=0; i<row; i++) {
                String key = "";
                for (int j=0; j<column; j++) {
                    // 현재 조합(mask) 에 대해 선택된 j가 포함되어있는지 확인
                    if ((mask & (1<<j)) != 0) {
                        key += relation[i][j] + "|";
                    }
                }
                set.add(key);
            }
            
            // 모든 행을 구별할 수 있는 지 개수 확인
            if (set.size() == row) {
                candidateKeys.add(mask);
            }
        }
        return candidateKeys.size();
    }
}