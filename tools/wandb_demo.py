# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import wandb

# wandb.init(project="test-project", entity="v587")
import random

# Launch 5 simulated experiments
total_runs = 5
for run in range(total_runs):
    # 🐝 1️⃣ Start a new run to track this script
    wandb.init(
        # Set the project where this run will be logged
        project="basic-intro",
        # We pass a run name (otherwise it’ll be randomly assigned, like sunshine-lollypop-10)
        name=f"experiment_{run}",
        entity="v587",
        # Track hyperparameters and run metadata
        config={
            "learning_rate": 0.02,
            "architecture": "CNN",
            "dataset": "CIFAR-100",
            "epochs": 10,
        })

    # This simple block simulates a training loop logging metrics
    epochs = 10
    offset = random.random() / 5
    for epoch in range(2, epochs):
        acc = 1 - 2 ** -epoch - random.random() / epoch - offset
        loss = 2 ** -epoch + random.random() / epoch + offset

        # 🐝 2️⃣ Log metrics from your script to W&B
        wandb.log({"acc": acc, "loss": loss})

    # Mark the run as finished
    wandb.finish()
