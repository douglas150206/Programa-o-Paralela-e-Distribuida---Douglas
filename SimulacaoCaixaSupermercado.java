import java.util.Random;
public class SimulacaoCaixaSupermercado {

    private int numeroCaixas = 1;           
    private int nClientes = 100;           
    private double mu = 5.0;               
    private double sigma = 0.5;            

    private static final double EPSILON = 0.1; 
    private final Random rng = new Random(42); 

    public void setNumeroCaixas(int n) { this.numeroCaixas = Math.max(1, n); }
    public void setNClientes(int n)      { this.nClientes = Math.max(1, n); }
    public void setMu(double mu)         { this.mu = mu; }
    public void setSigma(double sigma)   { this.sigma = Math.max(0.0, sigma); }

    private double amostraTruncada() {
        double z = rng.nextGaussian();       
        double s = mu + sigma * z;           
        return (s < EPSILON) ? EPSILON : s;  
    }

    public double simular() {
        double soma = 0.0;
        for (int i = 0; i < nClientes; i++) {
            soma += amostraTruncada();
        }
        return soma / nClientes;
    }
}
