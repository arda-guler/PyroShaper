class cell:
    def __init__(self, idx, x, y, e, n, w, s, isfuel=False):
        self.idx = idx
        self.x = x
        self.y = y
        self.e = e
        self.n = n
        self.w = w
        self.s = s
        
        self.fuel = 0
        if isfuel:
            self.fuel = 10
            
        self.active = False

    def get_burn_rate(self, msh):
        if not self.active:
            return 0

        burn_rate = 4
        
        if self.e and msh.cells[self.e].fuel > 0:
            burn_rate -= 1

        if self.n and msh.cells[self.n].fuel > 0:
            burn_rate -= 1

        if self.w and msh.cells[self.w].fuel > 0:
            burn_rate -= 1

        if self.s and msh.cells[self.s].fuel > 0:
            burn_rate -= 1

        return burn_rate

    def update_active(self, msh):
        if self.fuel <= 0:
            self.fuel = 0
            self.active = False
            return

        if self.e and msh.cells[self.e].active and msh.cells[self.e].get_burn_rate(msh) > 0:
            self.active = True

        if self.n and msh.cells[self.n].active and msh.cells[self.n].get_burn_rate(msh) > 0:
            self.active = True

        if self.w and msh.cells[self.w].active and msh.cells[self.w].get_burn_rate(msh) > 0:
            self.active = True

        if self.s and msh.cells[self.s].active and msh.cells[self.s].get_burn_rate(msh) > 0:
            self.active = True

    def update(self, msh, dt):
        self.update_active(msh)
        if self.active:
            self.burn_rate = self.get_burn_rate(msh)
            self.fuel -= self.burn_rate * dt

class mesh:
    def __init__(self, Nx, Ny):
        self.Nx = Nx
        self.Ny = Ny

        self.cells = [None] * Ny * Nx
        for j in range(Ny):
            for i in range(Nx):
                abs_idx = j * Nx + i

                e = j * Nx + (i + 1)
                n = (j+1) * Nx + i
                w = j * Nx + (i - 1)
                s = (j-1) * Nx + i

                if j == Ny-1:
                    n = None
                elif j == 0:
                    s = None

                if i == Nx-1:
                    e = None
                elif i == 0:
                    w = None
                    
                self.cells[abs_idx] = cell(abs_idx, i, j, e, n, w, s, False)
