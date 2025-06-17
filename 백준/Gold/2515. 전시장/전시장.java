
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static class SegmentTree {
        private int leafNodes;
        private int[] tree;
        SegmentTree(int maxHeight) {
            int leafNodes = 1;
            while (leafNodes <= (maxHeight+1)){
                leafNodes <<= 1;
            }
            this.leafNodes = leafNodes;
            int treeSize = 2 * leafNodes - 1;
            this.tree = new int[treeSize];
        }
        

        public int update(int targetHeight, int valueCost) {
            int left = 0;
            int right = this.leafNodes-1;
            int node = 0;

            int leftNode = node * 2 + 1;
            int rightNode = node * 2 + 2;
            int mid = (left + right) / 2;
            int ret;
            int compare;
            if (targetHeight <= mid) {
                ret = update(targetHeight, valueCost, left, mid, leftNode);
                compare = this.tree[rightNode];
            } else {
                ret = update(targetHeight, valueCost, mid+1, right, rightNode);
                compare = this.tree[leftNode];
            }
            if (ret > compare) {
                this.tree[node] = ret;
            } else {
                this.tree[node] = compare;
            }
            return this.tree[node];
        }

        public int update(int targetHeight, int valueCost, int left, int right, int node) {
            if (left == right) {
                if (this.tree[node] > valueCost) return this.tree[node];
                this.tree[node] = valueCost;
                return valueCost;
            }

            int leftNode = node * 2 + 1;
            int rightNode = node * 2 + 2;
            int mid = (left + right) / 2;
            int ret;
            int compare;
            if (targetHeight <= mid) {
                ret = update(targetHeight, valueCost, left, mid, leftNode);
                compare = this.tree[rightNode];
            } else {
                ret = update(targetHeight, valueCost, mid+1, right, rightNode);
                compare = this.tree[leftNode];
            }
            if (ret > compare) {
                this.tree[node] = ret;
            } else {
                this.tree[node] = compare;
            }
            return this.tree[node];
        }

        public int getCost(int targetHeight) {
            
            int left = 0;
            int right = this.leafNodes-1;
            int node = 0;

            int leftNode = node * 2 + 1;
            int rightNode = node * 2 + 2;
            int mid = (left + right) / 2;
            int ret = 0;
            if (targetHeight == mid) {
                return this.tree[leftNode];
            } else if (targetHeight < mid) {
                return getCost(targetHeight, left, mid, leftNode);
            } else {
                int compare = this.tree[leftNode];
                ret = getCost(targetHeight, mid+1, right, rightNode);
                if (ret < compare) {
                    return compare;
                }
                return ret;
            }
        }

        public int getCost(int targetHeight, int left, int right, int node) {
            // 0부터 right 까지라서 left와 타깃을 비교할 필요는 없음
            if (left == right) {
                return this.tree[node];
            }

            int leftNode = node * 2 + 1;
            int rightNode = node * 2 + 2;
            int mid = (left + right) / 2;
            int ret = 0;
            if (targetHeight == mid) {
                return this.tree[leftNode];
            } else if (targetHeight < mid) {
                return getCost(targetHeight, left, mid, leftNode);
            } else {
                int compare = this.tree[leftNode];
                ret = getCost(targetHeight, mid+1, right, rightNode);
                if (ret < compare) {
                    return compare;
                }
                return ret;
            }
        }

        int peek() {
            return this.tree[0];
        }
        
    }

    private static class Picture {
        int height;
        int cost;
        Picture(int h, int c) {
            this.height = h;
            this.cost = c;
        }
    }
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        Picture[] pictures = new Picture[n];
        int maxHeight = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            pictures[i] = new Picture(h, c);
            if (h > maxHeight) {
                maxHeight = h;
            }
            
        }
        Arrays.sort(pictures, (Picture a, Picture b)->a.height - b.height);
        SegmentTree tree = new SegmentTree(maxHeight);
        // 연산 시작
        for (int i = 0; i < n; i++) {
            Picture pic = pictures[i];
            int maxCost = tree.getCost(pic.height-s);
            tree.update(pic.height, maxCost + pic.cost);
        }
        System.out.println(tree.peek());
    }

    

}
