public class Filosofo {

    private final int numero;
    private final Garfo garfoEsq;
    private final Garfo garfoDir;

    public Filosofo(int numero, Garfo garfoEsq, Garfo garfoDir) {
        this.numero = numero;
        this.garfoEsq = garfoEsq;
        this.garfoDir = garfoDir;
    }

    public int getNumero() {
        return numero;
    }

    public Garfo getGarfoEsquerda() {
        return garfoEsq;
    }

    public Garfo getGarfoDireita() {
        return garfoDir;
    }
}
