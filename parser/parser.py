import argparse



if __name__ == "__main__":
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description="Training script parameters")
    lp = ModelParams(parser)
    op = OptimizationParams(parser)
    pp = PipelineParams(parser)

    # 解析命令行参数
    args = parser.parse_args()

    print(f"Model name: {args.model_name}")
    print(f"Learning rate: {args.learning_rate}")
    print(f"Number of steps: {args.num_steps}")