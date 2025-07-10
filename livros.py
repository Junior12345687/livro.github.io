class Recomendacao:
    def __init__(self):
        self.livros = []
        self.palavras_positivas = {'amo', 'adorei', 'gostei', 'maravilhoso', 'incrivel'}
        self.palavras_negativas = {'não gostei', 'odiei', 'ruim', 'péssimo'}

    def cadastro_de_livro(self, titulo, autor, genero, nota):
        for livro in self.livros:
            if livro['titulo'].lower() == titulo.lower() and livro['autor'].lower() == autor.lower():
                print(f"O livro '{titulo}' do {autor} ja esta cadastrado!")
                return
            
        self.livros.append({
            'titulo': titulo,
            'autor': autor,
            'genero':genero,
            'nota': nota,
        })

    def recomendacao_por_genro(self, genero_desejado):
        recomendados = [livro for livro in self.livros
                        if livro ['genero'].lower() == genero_desejado.lower()]
        
        if not recomendados:
            print(f"Nenhum livro do genero '{genero_desejado}' encontrado")
            return
        
        print(f"\nLivros do genero '{genero_desejado}':")
        for livro in sorted(recomendados, key=lambda x: x['nota'], reverse=True):
            print(f"- {livro['titulo']} ({livro['autor']}) - Nota: {livro['nota']}")
                    
    def analise_de_sentimento(self, texto):
        positivas = sum(1 for p in texto.lower().split() if p in self.palavras_positivas)
        negativas = sum(1 for p in texto.lower().split() if p in self.palavras_negativas)

        if positivas > negativas:
            return 'positivo'
        elif negativas > positivas:
            return 'negativa'
        return 'neutro'
    
    def adicionar_avaliacao(self, titulo, texto):
        for livro in self.livros:
            if livro['titulo'].lower() == titulo.lower():
                sentimento = self.analise_de_sentimento(texto)
                livro['avaliacoes'].append({
                    'texto': texto,
                    'sentimento': sentimento
                })

                if sentimento == 'positivo':
                    livro['nota'] = min(5, livro['nota'] + 0.2)
                elif sentimento == 'negativo':
                    livro['nota'] = min(0, livro['nota'] - 0.2)
                
                print("Avaliação registrada!")
                return True
        print("Livro não encontrado!")
        return False
        
    def exibir_avaliacoes(self, titulo):
        for livro in self.livros:
            if livro['titulo'].lower() == titulo.lower():
                if not livro['avaliacoes']:
                    print("Nenhuma avaliação ainda!")
                    return
                
                print(f"\nAvaliações para '{livro[titulo]}':")
                for av in livro['avaliacoes']:
                    print(f"- {av['texto']} [{av['sentimento']}]")
                    return
            
            print("Livro nao encotrado!")

def menu():
    sistema = Recomendacao()

    sistema.cadastro_de_livro("1984", "George Orwell", "Ficção", 4.5)
    sistema.cadastro_de_livro("Duna", "Frank Herber", "Ficção", 4.8)
    
    while True:
        print("\n===Sistema de Recomendação de Livros===")
        print("1. Buscar por genero")
        print("2. Adicionar avaliaçao")
        print("3. Ver avaliação")
        print("4. Sair")
    
        opcao = input("Opção:")

        if opcao == "1":
            genero = input("Genero desejado: ")
            sistema.recomendacao_por_genro(genero)
        
        elif opcao == "2":
            titulo = input("Titulo do livro:")
            texto = input("Sua avaliação")
            sistema.adicionar_avaliacao(titulo, texto)
        
        elif opcao == "3":
            titulo = input("Titulo do livro:")
            sistema.mostrar_avaliacao(titulo)
        
        elif opcao == "4":
            print("saindo...")
            break

        else:
            print("Opção invalido!")

if __name__ == "__main__":
    menu()