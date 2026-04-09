defmodule Chat do
  def iniciar do
    entradas = ["oi", "teste", "erro grande aqui", "ok", "sair"]
    loop([], entradas)
  end

  def loop(mensagens, []), do: IO.puts("Fim")

  def loop(mensagens, [entrada | resto]) do
    IO.puts("\nEntrada: #{entrada}")

    # ❌ PROBLEMA: muita responsabilidade aqui
    if entrada == "sair" do
      IO.puts("Encerrando...")
    else
      novas = mensagens ++ [entrada]

      Enum.each(novas, fn m ->
        IO.puts(m)
      end)

      loop(novas, resto)
    end
  end
end

Chat.iniciar()
