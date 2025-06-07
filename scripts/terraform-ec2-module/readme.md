Descrição dos arquivos:

versions.tf: controla a versão do Terraform e dos providers.

provider.tf: configura o provider AWS.
main.tf: faz referência ao módulo que cria a instância EC2.

variables.tf: define variáveis globais (se necessário).

modules/ec2/main.tf: define os recursos (Security Group, EC2) que serão criados.

modules/ec2/variables.tf: variáveis específicas do módulo.

modules/ec2/outputs.tf: expõe variáveis de saída do módulo.