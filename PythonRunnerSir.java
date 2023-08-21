import java.io.*;

// docName에 파일 이름 해서 실행하셈~
// sir.py : pdf에서 텍스트 추출해서 민감 정보 감지

public class PythonRunnerSir {
    public static void main(String[] args) throws IOException, InterruptedException {

        String docName = "test";

        // activate anaconda virtual environment, execute python file
        // 오토인코더 하느라 가상환경 아나콘다말고 다른걸로 바꿨는데 그걸로 할라니까 안되네
        // 전이랑 똑같이 해놨으니까 너 컴퓨터에선 되겠지 뭐 수고~
        ProcessBuilder pb = new ProcessBuilder();
        pb.directory(new File("/Users/seungtoc/Desktop/SIR"));
        pb.command("/Users/seungtoc/anaconda3/bin/conda", "run", "-n", "zero", "python", "sir.py", docName);
        
        pb.redirectErrorStream(true);
        
        Process process = pb.start();

        // get outputs
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }

        //  for confirmation
        int exitCode = process.waitFor();
        if (exitCode == 0) {
            System.out.println("sir.py executed successfully.");
        } else {
            System.out.println("sir.py execution failed.");

             // Print error messages
             InputStream errorStream = process.getErrorStream();
             BufferedReader errorReader = new BufferedReader(new InputStreamReader(errorStream));
             String errorLine;
             while ((errorLine = errorReader.readLine()) != null) {
                 System.out.println("Error: " + errorLine);
             }
        }
    }
}