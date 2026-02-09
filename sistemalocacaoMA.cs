using System;
using System.Collections.Generic;

namespace LocalizaClone
{
    // O "Estado" do carro - Isso mostra que você entende o fluxo real
    public enum StatusVeiculo
    {
        Disponivel,
        Alugado,
        EmLavagem,
        Manutencao,
        Vistoria
    }

    public class Veiculo
    {
        public string Placa { get; set; }
        public string Modelo { get; set; }
        public StatusVeiculo Status { get; set; }
        public int Quilometragem { get; set; }
        public bool TanqueCheio { get; set; }

        public Veiculo(string placa, string modelo, int km)
        {
            Placa = placa;
            Modelo = modelo;
            Status = StatusVeiculo.Disponivel; // Todo carro nasce disponível
            Quilometragem = km;
            TanqueCheio = true;
        }
    }

    public class OperacaoLocadora
    {
        // Método para realizar a SAÍDA do carro (Check-out)
        public void RealizarLocacao(Veiculo carro, string cnhMotorista)
        {
            if (carro.Status == StatusVeiculo.Disponivel)
            {
                carro.Status = StatusVeiculo.Alugado;
                Console.WriteLine($"[SUCESSO] Veículo {carro.Modelo} ({carro.Placa}) alugado para CNH {cnhMotorista}.");
                Console.WriteLine("-> Status atualizado para: ALUGADO");
            }
            else
            {
                Console.WriteLine($"[ERRO] O veículo {carro.Modelo} não está disponível. Status atual: {carro.Status}");
            }
        }

        // Método para realizar a DEVOLUÇÃO (Check-in) com regras de negócio
        public void RealizarDevolucao(Veiculo carro, int kmFinal, bool devolveuTanqueCheio)
        {
            Console.WriteLine($"\n--- INICIANDO VISTORIA DE DEVOLUÇÃO: {carro.Modelo} ---");

            // 1. Atualiza KM
            int kmRodados = kmFinal - carro.Quilometragem;
            carro.Quilometragem = kmFinal;
            Console.WriteLine($"KM Rodados: {kmRodados}km");

            // 2. Regra de Negócio: Cobrança de Combustível
            decimal taxaCombustivel = 0;
            if (!devolveuTanqueCheio)
            {
                taxaCombustivel = 150.00m; // Taxa fixa simulada
                Console.WriteLine($"[ALERTA] Cliente não encheu o tanque. Taxa de R$ {taxaCombustivel} aplicada.");
            }

            // 3. Regra de Negócio: Carro sujo vai para lavagem, não para o pátio
            carro.Status = StatusVeiculo.EmLavagem;
            carro.TanqueCheio = devolveuTanqueCheio;

            Console.WriteLine($"Processo finalizado. Veículo enviado para LAVAGEM.");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Cenário de Teste
            Veiculo onix = new Veiculo("ABC-1234", "Chevrolet Onix", 50000);
            OperacaoLocadora sistema = new OperacaoLocadora();

            // 1. Tentativa de Locação
            sistema.RealizarLocacao(onix, "123.456.789-00");

            // 2. Simulação de Devolução (Cliente não encheu o tanque)
            sistema.RealizarDevolucao(onix, 50200, false);
        }
    }
}
