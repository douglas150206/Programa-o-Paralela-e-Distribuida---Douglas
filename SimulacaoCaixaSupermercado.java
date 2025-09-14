import java.util.Arrays;
import java.util.Random;

public class SimulacaoCaixaSupermercado {

    private int numeroCaixas = 1;
    private int quantidadeClientes = 100;
    private double mediaTempoAtendimento = 5.0;
    private double desvioPadraoTempoAtendimento = 0.5;

    private static final double TEMPO_MINIMO_ATENDIMENTO = 0.1;

    private final Random rng;

    public SimulacaoCaixaSupermercado(long seed) {
        this.rng = new Random(seed);
    }

    public void setNumeroCaixas(int n) {
        this.numeroCaixas = Math.max(1, n);
    }

    public void setQuantidadeClientes(int n) {
        this.quantidadeClientes = Math.max(1, n);
    }

    public void setMediaTempoAtendimento(double mu) {
        this.mediaTempoAtendimento = mu;
    }

    public void setDesvioPadraoTempoAtendimento(double sigma) {
        this.desvioPadraoTempoAtendimento = Math.max(0.0, sigma);
    }

    private double amostraTempoAtendimento() {
        double z = rng.nextGaussian();
        double t = mediaTempoAtendimento + desvioPadraoTempoAtendimento * z;
        return (t < TEMPO_MINIMO_ATENDIMENTO) ? TEMPO_MINIMO_ATENDIMENTO : t;
    }

    public double simularMediaTempoNoSistema() {
        double[] livreEm = new double[numeroCaixas]; 
        Arrays.fill(livreEm, 0.0);

        double somaTempoNoSistema = 0.0;

        for (int i = 0; i < quantidadeClientes; i++) {
            int idx = 0;
            for (int c = 1; c < numeroCaixas; c++) {
                if (livreEm[c] < livreEm[idx]) idx = c;
            }

            double s = amostraTempoAtendimento();      
            double inicio = livreEm[idx];              
            double fim = inicio + s;                   

            livreEm[idx] = fim;                        
            somaTempoNoSistema += fim;                 
        }

        return somaTempoNoSistema / quantidadeClientes;
    }
}
