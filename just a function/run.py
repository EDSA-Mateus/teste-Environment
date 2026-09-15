import argparse
import yaml

from calculator import calculate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", choices=["dev", "prod"], required=True)
    args = parser.parse_args()

    with open(f"config/{args.env}.yaml") as f:
        cfg = yaml.safe_load(f)

    result = calculate(3, 4, multiplier=cfg["multiplier"])
    print(f"[{cfg['label']}] Result: {result}")


if __name__ == "__main__":
    main()
