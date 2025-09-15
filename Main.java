import java.util.ArrayList;
import java.util.List;

public class Main {

    private static double media(List<Double> xs) {
        double s = 0.0;
        for (double x : xs) s += x;
        return s / xs.size();
    }

    private static double desvioPadrao(List<Double> xs, double m) {
        double s2 = 0.0;
        for (double x : xs) {
            double d = x - m;
            s2 += d * d;
        }
        return Math.sqrt(s2 / (xs.size() - 1));
    }

    private static void rodar(String rotulo, int nRodadas, int nClientes, int nCaixas, double mu, double sigma) {
        SimulacaoCaixaSupermercado sim = new SimulacaoCaixaSupermercado();
        sim.setNClientes(nClientes);
        sim.setNumeroCaixas(nCaixas); 
        sim.setMu(mu);
        sim.setSigma(sigma);

        List<Double> mediasDasRodadas = new ArrayList<>();

        for (int i = 0; i < nRodadas; i++) {
            double m = sim.simular();             
            mediasDasRodadas.add(m);
        }

        double mFinal = media(mediasDasRodadas);         
        double dpFinal = desvioPadrao(mediasDasRodadas, mFinal);

        System.out.printf("%s%n", rotulo);
        System.out.printf("  media_das_medias  ~ %.4f min%n", mFinal);
        System.out.printf("  dp_das_medias     ~ %.4f min%n%n", dpFinal);
    }

    public static void main(String[] args) {
        final int RODADAS  = 1000;
        final int N        = 100;
        final double MU    = 5.0;
        final double SIGMA = 0.5;
   
        rodar("Item 1: mu=5.0, sigma=0.5, N=100, rodadas=1000, caixas=1",
                RODADAS, N, 1, MU, SIGMA);

        rodar("Item 2.1: caixas=1 (mesmos params)", RODADAS, N, 1, MU, SIGMA);
        rodar("Item 2.2: caixas=2 (mesmos params)", RODADAS, N, 2, MU, SIGMA);
        rodar("Item 2.3: caixas=3 (mesmos params)", RODADAS, N, 3, MU, SIGMA);

        rodar("Item 3.1: mu=5.0, sigma=0.25, N=100", RODADAS, N, 1, 5.0, 0.25);
        rodar("Item 3.2: mu=5.0, sigma=1.0 , N=100", RODADAS, N, 1, 5.0, 1.0);
        rodar("Item 3.3: mu=5.0, sigma=2.0 , N=100", RODADAS, N, 1, 5.0, 2.0);
    }
}
