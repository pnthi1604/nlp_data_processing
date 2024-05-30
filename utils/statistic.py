import matplotlib.pyplot as plt

def draw_graph(title, xlabel, ylabel, data, steps, save_path=None):
    try:
        plt.plot(steps, data)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        if save_path is not None:
            plt.savefig(save_path)
        plt.show()
        plt.close()
    except Exception as e:
        print(e)

def draw_hist_graph(title, xlabel, ylabel, data, bins=20, save_path=None):
    try:
        plt.hist(data, bins=bins)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        if save_path is not None:
            plt.savefig(save_path)
        plt.show()
        plt.close()
    except Exception as e:
        print(e)

def get_length_tokens(tokenizer, dataset):
    return [len(tokenizer.encode(x).ids) for x in dataset]

__all__ = ['draw_graph', 'draw_hist_graph', 'get_length_tokens']