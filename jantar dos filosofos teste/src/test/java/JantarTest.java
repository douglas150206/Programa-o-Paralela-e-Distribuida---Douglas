import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class JantarTest {

    private Jantar refeicao;

    @BeforeEach
    void preparar() {
        refeicao = new Jantar();
    }

    @Test
    void deveInicializarEstruturasCorretamente() {
        refeicao.iniciar();

        List<Filosofo> grupo = refeicao.getFilosofos();
        List<Garfo> utensilios = refeicao.getGarfos();

        assertNotNull(grupo, "A lista de participantes não pode ser nula.");
        assertEquals(5, grupo.size(), "Devem existir cinco filósofos configurados.");

        assertNotNull(utensilios, "A lista de talheres não pode ser nula.");
        assertEquals(5, utensilios.size(), "Devem existir cinco garfos disponíveis.");

        for (Filosofo f : grupo) {
            assertNotNull(f.getGarfoEsquerda(), "Filósofo deve ter garfo do lado esquerdo.");
            assertNotNull(f.getGarfoDireita(), "Filósofo deve ter garfo do lado direito.");
            assertNotEquals(f.getGarfoEsquerda(), f.getGarfoDireita(),
                    "Os dois garfos do filósofo devem ser diferentes.");
        }

        assertSame(utensilios.get(0), grupo.get(0).getGarfoEsquerda(),
                "Falha proposital: este teste não deve passar.");

        assertTrue(refeicao.isAtivo(), "O jantar deveria estar marcado como iniciado.");
    }
}
