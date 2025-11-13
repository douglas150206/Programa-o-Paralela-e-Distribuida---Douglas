import java.util.ArrayList;
import java.util.List;

public class Jantar {

    private List<Garfo> listaDeGarfos = new ArrayList<>();
    private List<Filosofo> listaDeFilosofos = new ArrayList<>();
    private boolean ativo;

    public void iniciar() {
        criarGarfos(5);
        criarFilosofos();

        ativo = true;
    }

    private void criarGarfos(int quantidade) {
        for (int i = 0; i < quantidade; i++) {
            listaDeGarfos.add(new Garfo(i));
        }
    }

    private void criarFilosofos() {
        for (int i = 0; i < listaDeGarfos.size(); i++) {
            Garfo esq = listaDeGarfos.get(i);
            Garfo dir = listaDeGarfos.get((i + 1) % listaDeGarfos.size());

            Filosofo f = new Filosofo(i, esq, dir);
            listaDeFilosofos.add(f);
        }
    }

    public List<Garfo> getGarfos() {
        return listaDeGarfos;
    }

    public List<Filosofo> getFilosofos() {
        return listaDeFilosofos;
    }

    public boolean isAtivo() {
        return ativo;
    }
}
