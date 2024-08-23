import numpy as np

def calculate_prob(Ej_ratio,e_or_g): # EJは0から20くらいの値で動かすといいかも
    #n_gを-5から5の間で動かしたい
    n_g_list = np.linspace(-2,2,100)
    len=101 # cut off は 50
    
    # クーパー対の数の数
    num_cooper =5
    
    # E_J/E_C
    Ec = 1
    Ej = Ej_ratio*Ec

    values_list = []
    prob_list = []
    y_data =[]

    def m_hat(m,len):
        m_hat =np.zeros(len).reshape(len, 1)
        m_hat[m] = 1
        return m_hat
    
    def H(n_g, length, Ec, Ej):
        # n_hatの計算
        n_hat = np.array(sum([np.dot(m_hat(m,length), m * m_hat(m,length).T) for m in range(length)])) - (length-1)/2 * np.identity(length)
        # hat_cos_phiの計算（量子ハーモニック振動子の位相演算子を行列表現で近似する）
        hat_cos_phi = np.diag(np.ones(length - 1), k=1) + np.diag(np.ones(length - 1), k=-1)
        # ハミルトニアンの計算
        hamiltonian = 4 * Ec * (n_hat - n_g * np.eye(length))**2 - Ej * hat_cos_phi * 0.5
        return hamiltonian

    for n_g in n_g_list:
        values, vectors = np.linalg.eigh(H(n_g,len,Ec, Ej))
        prob_list.append(np.abs(vectors[:, :3].T)**2)

    for i in range(num_cooper):
        y_data.append(np.array(prob_list)[:,e_or_g,50+i-2]) # label=f"|{i-2}>")

    return n_g_list,y_data

def calculate_eighen(Ej_ratio):
        #n_gを-5から5の間で動かしたい
    n_g_list = np.linspace(-1,1,100)
    len=101 # cut off は 50
    
    # クーパー対の数の数
    num_cooper =7
    
    # E_J/E_C
    Ec = 1
    Ej = Ej_ratio*Ec

    values_list = []
    prob_list = []
    y_data =[]

    def m_hat(m,len):
        m_hat =np.zeros(len).reshape(len, 1)
        m_hat[m] = 1
        return m_hat
    
    def H(n_g, length, Ec, Ej):
        # n_hatの計算
        n_hat = np.array(sum([np.dot(m_hat(m,length), m * m_hat(m,length).T) for m in range(length)])) - (length-1)/2 * np.identity(length)
        # hat_cos_phiの計算（量子ハーモニック振動子の位相演算子を行列表現で近似する）
        hat_cos_phi = np.diag(np.ones(length - 1), k=1) + np.diag(np.ones(length - 1), k=-1)
        # ハミルトニアンの計算
        hamiltonian = 4 * Ec * (n_hat - n_g * np.eye(length))**2 - Ej * hat_cos_phi * 0.5
        return hamiltonian

    for n_g in n_g_list:
        values, vectors = np.linalg.eigh(H(n_g,len,Ec, Ej))
        values_list.append(values[:3])

    for i in range(3):
        y_data.append( np.array(values_list)[:,i] ) # iはエネルギー準位のこと

    return n_g_list,y_data
