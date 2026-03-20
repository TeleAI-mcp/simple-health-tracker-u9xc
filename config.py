"""Configuration module for Simple Health Tracker."""

import os

class Config:
    """Application configuration settings."""
    
    DEBUG = os.environ.get('DEBUG', False)
    DATABASE_PATH = os.environ.get('DATABASE_PATH', 'data/health.db')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    @classmethod
    def to_dict(cls):
        """Return config as dictionary."""
        return {
            'DEBUG': cls.DEBUG,
            'DATABASE_PATH': cls.DATABASE_PATH,
            'LOG_LEVEL': cls.LOG_LEVEL
        }