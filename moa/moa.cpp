#include <iostream>
#include <vector>
#include <string> 
#include <assert.h>
using namespace std;



class Vertice {
public:
	int tabuleiro[4][4];
	int distInicio;
	int distFinal;
	Vertice *pai;
	vector<Vertice> adj;
	bool pertenceLista;
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
		pertenceLista = false;
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
		pertenceLista = false;
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

int minElement(vector<Vertice> A){
	int min, i, aux = 0,aux2 = A.size();
	
	min = A[0].distInicio + A[0].distFinal;
	for(i = 0; i < aux2; i ++){
		int f = A[i].distInicio + A[i].distFinal;
		// A[i].print();	
		if(f<min){
			min = f;
			aux = i;
		}
	}

	return aux;

}

void swap (Vertice &u, int i, int j, int x, int y){
	// cout << "Antes troca " << u.tabuleiro[i][j] << " ";
	// cout << u.tabuleiro[x][y] << endl;
	int aux;
	aux = u.tabuleiro[i][j];
	u.tabuleiro[i][j] = u.tabuleiro[x][y];
	u.tabuleiro[x][y] = aux;

	// cout << "Depois troca " << u.tabuleiro[i][j] << " ";
	// cout << u.tabuleiro[x][y] << endl;
}

int comparaMatriz(int m1[4][4],int m2[4][4]){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(m1[i][j] != m2[i][j]){
				return 0;
			}
		}
	}
	return 1;
}

int comparaVertices(vector<Vertice> list, Vertice u ){
	Vertice v;
	int aux = list.size();
	for(int i = 0; i <aux;  i++){
		v = list[i];
		if(comparaMatriz(u.tabuleiro, v.tabuleiro) ){
			return i;
		}
	}
	return -1;
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



int AStar(Vertice u){
	// g(s) -> menor dist ate inicio || h(n) -> menor dist ate final 

	int achouFinal, i, matrizFinal[4][4] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0};
	vector<Vertice> A,F,sucessores;
	Vertice final, v;
	u.pai = NULL;
	u.distFinal = h1(u.tabuleiro);
	u.distInicio = 0;
	u.pertenceLista = true;
	A.push_back(u);

	while(!A.empty()){

		i = minElement(A);
		v = A[i];
		A.erase(A.begin()+i);
		// v.print();
		F.push_back(v);
		
		achouFinal = comparaMatriz(v.tabuleiro, matrizFinal);
		if(achouFinal){
			final = v;
			break;
		}
		
		GeraSucessor(v, v.adj);
		

		for(Vertice &x: v.adj){
			
			int aux = comparaVertices(A,x);
			if(aux != -1){
				if(v.distInicio<A[aux].distInicio){
					cout << "PINTO " << endl; 
					A.erase(A.begin()+aux);
					F.push_back(x);
				}
			}

			
			int aux2 = comparaVertices(F,x); 

			if(aux == -1 && aux2 == -1){
				x.distFinal = h1(x.tabuleiro);
				A.push_back(x);
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
	Vertice v, u = getInput();
	

	cout << AStar(u);
	
	
	return 0;
}