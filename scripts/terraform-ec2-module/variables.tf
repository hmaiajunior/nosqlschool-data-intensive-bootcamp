# Define a variável region com um valor padrão de us-east-1.

variable "region" {
  type        = string
  description = "Regiao AWS onde os recursos serao criados"
  default     = "us-east-1"  # Você pode alterar conforme sua preferência
}
