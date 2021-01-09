import json
import os


class Config:
    def __init__(self):
        # pass
        self.working_path = self.new_working_path()
        self.abs_path = os.path.dirname(os.path.abspath(__file__))
        self.download_path = os.path.join(self.abs_path, 'download')
        os.makedirs(self.download_path, exist_ok=True)
        # 本地文件目录 压缩后得到的文件
        self.zip_file = ''
        self.ligands_path = []  # 输入ligands的文件夹
        self.ligands = []
        self.ligands_id = []
        self.ligands_headers = ['Name', 'Crystal\nStructure', 'Exp. Affinity (kcal/mol)', 'Exp. Error (kcal/mol)',
                                'Weight']
        self.prepare_headers = ['Name', 'Crystal\nStructure', 'Exp. Affinity (kcal/mol)', 'Exp. Error (kcal/mol)',
                                'Opts']
        self.has_exp_data = None

        self.simmat = None
        self.data_pos = None
        self.graph_doe = None

        self.pairs_headers = ['Ligand A', 'Ligand B', 'sim. score']
        self.pairs = []

        self.cycles_headers = ['num_of_nodes', 'nodes_in_cycle', 'hysteresis']
        self.config_data = ''
        self.username = ''
        self.license = ''
        self.working_path = ''
        self.jobs = ''
        self.base_url = ''
        self.job_id = ''
        self.config = "config.json"
        self.job_path = ''
        # 上传到dp_data的文件
        self.upload_path = ''

        self.Hermite_viewer = None
        self.Hermite_mapping_state = 0

    # 创建一个新的目录值
    def new_working_path(self):
        path = os.getcwd()
        max_index = -1
        for tmp_dir in os.listdir(path):
            if "work_" in tmp_dir:
                index = tmp_dir.split("work_")[-1]
                if index.isdigit():
                    index = int(index)
                    if max_index < index:
                        max_index = index
        max_index = max_index + 1
        path = os.path.join(path, 'work_%s' % max_index)
        return path

    # 获取相关的参数配置
    def get_config(self):
        self.config_data = json.loads(open(self.config).read())
        self.username = self.config_data.get("username", '')
        self.license = self.config_data.get("license", '')
        self.working_path = self.config_data.get("working_path", '')
        self.jobs = self.config_data.get("jobs", '')
        self.base_url = self.config_data.get("base_url", '')


config = Config()
