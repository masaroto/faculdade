#include <iostream>
#include <vector>
#include <string> 
#include <assert.h>
#include <unordered_map> 
#include <queue>
#include <cstdlib>
#include <time.h>
using namespace std;

class Vertice {
public:
	int tabuleiro[4][4];
	int distInicio;
	int distFinal;
	Vertice *pai;
	vector<Vertice> adj;
	int i;
	int j;
public:
	Vertice(){}
	Vertice(int tabela[4][4]){
		for (int x = 0; x < 4 ; x++){
		 	for (int y = 0; y < 4 ; y++){
		 		tabuleiro[x][y] = tabela[x][y];
				if (tabela[x][y]==0){
					
					i = x;
					j = y;
				 }
		 	}
		 }
	}
	Vertice(int tabela[4][4],int ini, Vertice u){

		for (int x = 0; x < 4 ; x++){
		 	for (int y = 0; y < 4 ; y++){
		 		tabuleiro[x][y] = tabela[x][y];
				if (tabela[x][y]==0){
					i = x;
					j = y;
				 }
		 	}
		 } 
		distInicio = ini;
		pai = &u;
	}
	void print(){
		int i = 0, j=0;
		string token = "";
		for (i = 0; i < 4 ; i++){
			for (j = 0; j < 4 ; j++){
				token += std::to_string(tabuleiro[i][j]);
				token += " ";
			}
			cout << token << endl;
			token = "";

		}
		cout << "Pai: " << pai << endl;
		cout << "Dist ate o final: " << distFinal << endl;
		cout << "Dist ate o inicio: " << distInicio << endl;
		cout << endl; 


	}	
};


bool operator<(const Vertice &u, const Vertice &v) {
	int UFinal = u.distInicio + u.distFinal, VFinal = v.distInicio + v.distFinal;
	return UFinal > VFinal;
}


string key(int tab[4][4]){
	string key = "";
	for (int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			key += to_string(tab[i][j]);
		}
	}
	return key;
}

void swap (Vertice &u, int i, int j, int x, int y){
	int aux;
	aux = u.tabuleiro[i][j];
	u.tabuleiro[i][j] = u.tabuleiro[x][y];
	u.tabuleiro[x][y] = aux;

}


Vertice getInput(){
	int tabela[4][4];
	for (int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			cin >> tabela[i][j];
		}
	}
	Vertice u = Vertice(tabela);
	
	return u;
}

void GeraSucessor(Vertice u, vector<Vertice> &list){
	Vertice v;
	if(u.i != 0){
		swap(u, u.i-1, u.j, u.i, u.j);
		v = Vertice(u.tabuleiro, u.distInicio+1,u);
		list.push_back(v);
		swap(u, u.i-1, u.j, u.i, u.j);
	}

	if(u.i != 3){
		swap(u, u.i+1, u.j, u.i, u.j);
		v = Vertice(u.tabuleiro, u.distInicio+1,u);
		list.push_back(v);
		swap(u, u.i, u.j, u.i+1, u.j);
	}

	if(u.j != 0){
		swap(u, u.i, u.j-1, u.i, u.j);
		v = Vertice(u.tabuleiro, u.distInicio+1,u);
		list.push_back(v);
		swap(u, u.i, u.j, u.i, u.j-1);
	}

	if(u.j != 3){
		swap(u, u.i, u.j+1, u.i, u.j);
		v = Vertice(u.tabuleiro, u.distInicio+1,u);
		list.push_back(v);
		swap(u, u.i, u.j, u.i, u.j+1);
	}
}
//heuristica 1
int h1(int tabela[4][4]){
	int num = 1;
	int foraLugar = 0;
	for (int i = 0; i < 4; i++){
		for(int j = 0; j < 4; ++j){
			if(tabela[i][j] != num){
				foraLugar++;
			}
			num++;
			if(num == 16){
				num = 0;
			}
		}
	}
	
	return foraLugar;
}

int h2(int tab[4][4]){
	int prox, soma = 0;
    for (int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(j == 3 && i == 3){
                break;
            }
            if(tab[i][j] != 0){

                prox = tab[i][j+1];
                if(j == 3 && i != 3){
                    prox = tab[i+1][0];
                } else if (prox == 0){
                    prox = 16;
                }

                if(tab[i][j] != prox - 1){
                    soma++;
                }

            }
		}
    }

    return soma;
}
int h3(int tab[4][4]){
	int num, coluna, linha, soma = 0;

	for (int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			num = (tab[i][j]);
            if(num != 0){
                linha = num / 4;
				//tratar caso o num esteja na ultima coluna
                if(num % 4 == 0 ){
                    linha = (num/4) -1;
                }
                
                coluna = num - (linha * 4) - 1;
            
                soma += abs(i - linha) + abs(j - coluna);
            }
		}
	}
	return soma;
}

float h4(int tab[4][4]){
    return 0.8*h3(tab) + 0.1*h2(tab) + 0.1*h1(tab);
}

int maximo(int a, int b, int c){
    return a > b ? (a > c ? a : c) : (b > c ? b : c);
}
float h5(int tab[4][4]){
    return maximo(h1(tab), h2(tab), h3(tab));
}

int AStar(Vertice u){
	// g(s) -> menor dist ate inicio || h(n) -> menor dist ate final 

	int achouFinal = 0;
	priority_queue<Vertice> A;
	unordered_map<string, Vertice> listaAberta, listaFechada;
	Vertice final, v;
	string pos, SucKey;
	bool pertenceA, pertenceF;

	//Inicializacao
	u.pai = NULL;
	u.distFinal = h5(u.tabuleiro);
	u.distInicio = 0;
	A.push(u);
	pos = key(u.tabuleiro);
	listaAberta[pos] = u;

	while(!listaAberta.empty()){

		v = A.top();
		A.pop();
		// cout << "Pai: " << endl;
		// v.print();
		pos = key(v.tabuleiro);
		listaFechada[pos] = v;

		if(v.distFinal == 0){
			final = v;
			achouFinal = 1;
			break;
		}
		
		GeraSucessor(v, v.adj);
		

		for(Vertice &x: v.adj){
			SucKey = key(x.tabuleiro);
			pertenceA = listaAberta.find(SucKey) != listaAberta.end();
			pertenceF = listaFechada.find(SucKey) != listaFechada.end();
			
			if(pertenceA){
				if(x.distInicio < listaAberta[SucKey].distInicio){
					listaAberta.erase(SucKey);
				}
			}
			pertenceA = listaAberta.find(SucKey) != listaAberta.end();
			if(!pertenceA && !pertenceF){
				x.distFinal = h3(x.tabuleiro);
				// cout << "Sucessores: " << endl;
				// x.print();
				listaAberta[SucKey] = x;
				A.push(x);
			}
		}

	}

	if(achouFinal){
		return final.distInicio;
	} else {
		return -1;
	}
}


int main(int argc, char const *argv[]){
	vector<Vertice> list;
	Vertice u = getInput();
	clock_t start, end;


	start = clock();
	cout << AStar(u) << endl;
	end = clock();

	double time_taken = double(end - start) / double(CLOCKS_PER_SEC); 
    cout << "Tempo: " << time_taken; 
    cout << " segundos " << endl;

	return 0;
}
