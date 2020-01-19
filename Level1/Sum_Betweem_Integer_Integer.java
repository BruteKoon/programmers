import java.util.ArrayList;
import java.util.Collections;
class Solution {
  public long solution(int a, int b) {
      long answer = 0;
      ArrayList<Integer> element = new ArrayList();
      element.add(a);
      element.add(b);
      Collections.sort(element);
      for(int k = element.get(0); k<element.get(1)+1; k++){
          answer = answer + k;
      }
      return answer;
  }
}
