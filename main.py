import mariadb
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 🔌 Conexão com o banco MariaDB
# ==========================================
try:
    conn = mariadb.connect(
        user="root",      
        password="",
        host="localhost",
        port=3306,
        database="techinfo"
    )
    print(" Conectado ao MariaDB com sucesso!")

except mariadb.Error as e:
    print(f" Erro ao conectar ao MariaDB: {e}")
    exit()


# ==========================================
# 📊 Consultando dados: Receita por vendedor
# ==========================================
query = """
SELECT 
    v.nome AS vendedor,
    SUM(p.preco * vd.quantidade) AS receita_total
FROM vendas vd
JOIN vendedores v ON vd.vendedor_id = v.id
JOIN produtos p ON vd.produto_id = p.id
GROUP BY v.nome
ORDER BY receita_total DESC;
"""
df = pd.read_sql(query, conn)

# Exibe os dados no console
print("\n📋 Receita por Vendedor:\n", df)

# ==========================================
# 📈 Criando o gráfico
# ==========================================
plt.figure(figsize=(8,5))
plt.bar(df['vendedor'], df['receita_total'], color='skyblue')
plt.title('Receita Total por Vendedor', fontsize=14)
plt.xlabel('Vendedor')
plt.ylabel('Receita (R$)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# ==========================================
# 🔒 Encerrando a conexão
# ==========================================
conn.close()