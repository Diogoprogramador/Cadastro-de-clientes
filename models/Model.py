import sqlite3


class BancoDados:

    def __init__(self):
        self._conexao = sqlite3.connect('banco.db')
        self._cursor = self._conexao.cursor()

    def criar_banco(self):
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS
                banco (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_cliente TEXT,
                    contato TEXT,
                    endereco TEXT,
                    pedido TEXT,
                    data_pedido TEXT,
                    data_prev_entrega TEXT,
                    status TEXT
                )
            """
        )

    def salvar(self, dados):
        self._cursor.execute(
            """
            INSERT INTO
                banco (
                    nome_cliente,
                    contato,
                    endereco,
                    pedido,
                    data_pedido,
                    data_prev_entrega,
                    status
                )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                dados['nome_cliente'],
                dados['contato_cliente'],
                dados['endereco'],
                dados['produto'],
                dados['data_calendario1'],
                dados['data_calendario2'],
                'Para Produção',
            )
        )

        # Salvando as alterações
        self._conexao.commit()

    def listar(self):
        self._cursor.execute("SELECT * FROM banco")

        return self._cursor.fetchall()

    def obter_cliente(self, dados):
        self._cursor.execute(
            "SELECT * FROM banco WHERE id = ? OR contato = ?",
            (dados['id_cliente'], dados['contato'],)
        )

        return self._cursor.fetchone()

    def obter_por_status(self, status_selecionado):
        self._cursor.execute(
            "SELECT * FROM banco WHERE status = ?", (status_selecionado,)
        )

        return self._cursor.fetchall()

    def atualizar(self, dados):
        self._cursor.execute(
            """
            UPDATE
                banco
            SET
                nome_cliente = ?,
                contato = ?,
                endereco = ?,
                pedido = ?,
                data_pedido = ?,
                data_prev_entrega = ?,
                status = ?
            WHERE
                id = ?
            """,
            (
                dados['novo_nome'],
                dados['novo_contato'],
                dados['novo_endereco'],
                dados['novo_pedido'],
                dados['data_pedido'],
                dados['data_entrega'],
                dados['status'],
                dados['indice'],
            )
        )

        self._conexao.commit()

    def excluir(self, indice):
        self._cursor.execute("DELETE FROM banco WHERE id = ?", (indice,))
        # Excluir o item da Treeview
        self._conexao.commit()
