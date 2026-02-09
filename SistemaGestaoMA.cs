using System;
using System.Collections.Generic;
using System.Linq;

namespace SistemaGestao
{
    // Classe que representa a entidade Cliente (Model)
    public class Cliente
    {
        public int Id { get; set; }
        public string Nome { get; set; }
        public string Email { get; set; }
        public bool Ativo { get; set; }

        public Cliente(int id, string nome, string email)
        {
            Id = id;
            Nome = nome;
            Email = email;
            Ativo = true;
        }
    }

    // Classe responsável pelas regras de negócio (Service)
    public class ClienteService
    {
        private List<Cliente> _bancoDeDadosFake = new List<Cliente>();

        // Método para Adicionar (CREATE)
        public void CadastrarCliente(string nome, string email)
        {
            int novoId = _bancoDeDadosFake.Count + 1;
            var novoCliente = new Cliente(novoId, nome, email);
            _bancoDeDadosFake.Add(novoCliente);
            Console.WriteLine($"Sucesso: Cliente {nome} cadastrado com ID {novoId}.");
        }

        // Método para Listar (READ)
        public void ListarClientesAtivos()
        {
            var ativos = _bancoDeDadosFake.Where(c => c.Ativo).ToList();
            Console.WriteLine("\n--- Clientes Ativos ---");
            foreach (var c in ativos)
            {
                Console.WriteLine($"ID: {c.Id} | Nome: {c.Nome} | Email: {c.Email}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Simulando a execução do sistema
            ClienteService servico = new ClienteService();

            Console.WriteLine("Iniciando Sistema de Gestão...");
            
            servico.CadastrarCliente("Marcos Alexandre", "marcos@exemplo.com");
            servico.CadastrarCliente("Empresa Tech", "contato@tech.com");

            servico.ListarClientesAtivos();
        }
    }
}
