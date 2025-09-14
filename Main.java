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

    private static void rodarExperimento(String rotulo, int mCaixas, int N, double mu, double sigma, int rodadas) {
        List<Double> medias = new ArrayList<>();

        for (int r = 0; r < rodadas; r++) {
            SimulacaoCaixaSupermercado sim = new SimulacaoCaixaSupermercado(42L + r);
            sim.setNumeroCaixas(mCaixas);
            sim.setQuantidadeClientes(N);
            sim.setMediaTempoAtendimento(mu);
            sim.setDesvioPadraoTempoAtendimento(sigma);

            double mediaRodada = sim.simularMediaTempoNoSistema();
            medias.add(mediaRodada);
        }

        double m = media(medias);
        double dp = desvioPadrao(medias, m);
        System.out.printf("%s -> média: %.3f min | desvio-padrão das médias: %.3f min (rodadas=%d)%n",
                rotulo, m, dp, rodadas);
    }

    public static void main(String[] args) {
        final int RODADAS = 1000;

        // 1) μ = 5.0, σ = 0.5, N=100, m=1
        rodarExperimento("Item 1: m=1, N=100, μ=5.0, σ=0.5",
                1, 100, 5.0, 0.5, RODADAS);

        // 2) variar número de caixas: 1, 2, 3 (mesmos N, μ, σ)
        rodarExperimento("Item 2: m=1, N=100, μ=5.0, σ=0.5",
                1, 100, 5.0, 0.5, RODADAS);
        rodarExperimento("Item 2: m=2, N=100, μ=5.0, σ=0.5",
                2, 100, 5.0, 0.5, RODADAS);
        rodarExperimento("Item 2: m=3, N=100, μ=5.0, σ=0.5",
                3, 100, 5.0, 0.5, RODADAS);

        // 3) variar σ: 0.25, 1.0, 2.0 (fixando m=1, N=100, μ=5.0)
        rodarExperimento("Item 3: m=1, N=100, μ=5.0, σ=0.25",
                1, 100, 5.0, 0.25, RODADAS);
        rodarExperimento("Item 3: m=1, N=100, μ=5.0, σ=1.0",
                1, 100, 5.0, 1.0, RODADAS);
        rodarExperimento("Item 3: m=1, N=100, μ=5.0, σ=2.0",
                1, 100, 5.0, 2.0, RODADAS);
    }
}
